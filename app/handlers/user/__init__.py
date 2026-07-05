from aiogram import Router
from .start import router as start_router
from .balance import router as balance_router
from .tasks import router as tasks_router
from .shop import router as shop_router

router = Router()
router.include_routers(start_router, balance_router, tasks_router, shop_router)