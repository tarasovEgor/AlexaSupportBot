__all__ = ("router", )

from aiogram import Router

from .base_commands import router as base_commands_router
from .gpt_commands import router as gpt_commands_router
from .common import router as common_router

router = Router(name=__name__)

router.include_router(base_commands_router)
router.include_router(gpt_commands_router)
router.include_router(common_router)