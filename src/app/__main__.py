# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import asyncio
import logging
from argparse import ArgumentParser
from logging import Logger
from typing import List, Optional

from environs import Env

from accelbyte_grpc_plugin.app import (
    App,
    AppOption,
    AppOptionGRPCInterceptor,
    AppOptionGRPCService,
)
from accelbyte_grpc_plugin.ctypes import PermissionAction
from accelbyte_grpc_plugin.utils import create_env

from .proto.cloudsaveValidatorService_pb2_grpc import (
    add_CloudsaveValidatorServiceServicer_to_server,
)
from .services.cloudsave_validator_service import (
    AsyncCloudsaveValidatorService,
)

DEFAULT_APP_PORT: int = 6565

DEFAULT_AB_BASE_URL: str = "https://test.accelbyte.io"
DEFAULT_AB_NAMESPACE: str = "accelbyte"
DEFAULT_AB_SECURITY_CLIENT_ID: Optional[str] = None
DEFAULT_AB_SECURITY_CLIENT_SECRET: Optional[str] = None

DEFAULT_ENABLE_HEALTH_CHECK: bool = True
DEFAULT_ENABLE_PROMETHEUS: bool = True
DEFAULT_ENABLE_REFLECTION: bool = True
DEFAULT_ENABLE_ZIPKIN: bool = True

DEFAULT_PLUGIN_GRPC_SERVER_AUTH_ENABLED: bool = False

DEFAULT_PLUGIN_GRPC_SERVER_LOGGING_ENABLED: bool = False
DEFAULT_PLUGIN_GRPC_SERVER_METRICS_ENABLED: bool = True


async def main(port: int, **kwargs) -> None:
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    env = create_env(**kwargs)

    options = create_options(env=env, logger=logger)
    options.append(
        AppOptionGRPCService(
            full_name=AsyncCloudsaveValidatorService.full_name,
            service=AsyncCloudsaveValidatorService(logger=logger),
            add_service_fn=add_CloudsaveValidatorServiceServicer_to_server,
        )
    )

    app = App(port=port, env=env, logger=logger, options=options)
    await app.run()


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "-p",
        "--port",
        default=DEFAULT_APP_PORT,
        type=int,
        required=False,
        help="[P]ort",
    )
    result = vars(parser.parse_args())
    return result


def create_options(env: Env, logger: Logger) -> List[AppOption]:
    options: List[AppOption] = []

    with env.prefixed("AB_"):
        base_url = env.str("BASE_URL", DEFAULT_AB_BASE_URL)
        namespace = env.str("NAMESPACE", DEFAULT_AB_NAMESPACE)
        client_id = env.str("CLIENT_ID", DEFAULT_AB_SECURITY_CLIENT_ID)
        client_secret = env.str(
            "CLIENT_SECRET", DEFAULT_AB_SECURITY_CLIENT_SECRET
        )

    with env.prefixed("ENABLE_"):
        if env.bool("HEALTH_CHECK", DEFAULT_ENABLE_HEALTH_CHECK):
            from accelbyte_grpc_plugin.options.grpc_health_check import (
                AppOptionGRPCHealthCheck,
            )

            options.append(AppOptionGRPCHealthCheck())
        if env.bool("PROMETHEUS", DEFAULT_ENABLE_PROMETHEUS):
            from accelbyte_grpc_plugin.options.prometheus import AppOptionPrometheus

            options.append(AppOptionPrometheus())
        if env.bool("REFLECTION", DEFAULT_ENABLE_REFLECTION):
            from accelbyte_grpc_plugin.options.grpc_reflection import (
                AppOptionGRPCReflection,
            )

            options.append(AppOptionGRPCReflection())
        if env.bool("ZIPKIN", DEFAULT_ENABLE_ZIPKIN):
            from accelbyte_grpc_plugin.options.zipkin import AppOptionZipkin

            options.append(AppOptionZipkin())

    with env.prefixed("PLUGIN_GRPC_SERVER_"):
        with env.prefixed("AUTH_"):
            if env.bool("ENABLED", DEFAULT_PLUGIN_GRPC_SERVER_AUTH_ENABLED):
                from accelbyte_py_sdk import AccelByteSDK
                from accelbyte_py_sdk.core import MyConfigRepository, InMemoryTokenRepository
                from accelbyte_py_sdk.token_validation.caching import CachingTokenValidator
                from accelbyte_py_sdk.services.auth import login_client, LoginClientTimer
                from accelbyte_grpc_plugin.interceptors.authorization import AuthorizationServerInterceptor

                config = MyConfigRepository(base_url, client_id, client_secret, namespace)
                token = InMemoryTokenRepository()
                sdk = AccelByteSDK()
                sdk.initialize(options={"config": config, "token": token})
                result, error = login_client(sdk=sdk)
                if error:
                    raise Exception(str(error))
                sdk.timer = LoginClientTimer(2880, repeats=-1, autostart=True, sdk=sdk)
                options.append(
                    AppOptionGRPCInterceptor(
                        interceptor=AuthorizationServerInterceptor(
                            resource=env.str("RESOURCE", None),
                            action=env.int("ACTION", None),
                            namespace=namespace,
                            token_validator=CachingTokenValidator(sdk=sdk),
                        )
                    )
                )
        if env.bool("LOGGING_ENABLED", DEFAULT_PLUGIN_GRPC_SERVER_LOGGING_ENABLED):
            from accelbyte_grpc_plugin.interceptors.logging import (
                LoggingServerInterceptor,
            )

            options.append(
                AppOptionGRPCInterceptor(
                    interceptor=LoggingServerInterceptor(logger=logger)
                )
            )

        if env.bool("METRICS_ENABLED", DEFAULT_PLUGIN_GRPC_SERVER_METRICS_ENABLED):
            from accelbyte_grpc_plugin.interceptors.metrics import (
                MetricsServerInterceptor,
            )

            options.append(
                AppOptionGRPCInterceptor(interceptor=MetricsServerInterceptor())
            )

    return options


if __name__ == "__main__":
    asyncio.run(main(**parse_args()))
