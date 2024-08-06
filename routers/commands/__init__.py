__all__ = ("router", )

from aiogram import Router

from .zammad_commands import router as zammad_commands_router
from .base_commands import router as base_commands_router
from .gpt_commands import router as gpt_commands_router
from .is_client_commands import router as is_client_commands_router
from .common import router as common_router

router = Router(name=__name__)

router.include_router(zammad_commands_router)
router.include_router(base_commands_router)
router.include_router(gpt_commands_router)
router.include_router(is_client_commands_router)
router.include_router(common_router)
