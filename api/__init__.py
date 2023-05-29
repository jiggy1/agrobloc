from fastapi import APIRouter
from api import user, stock, cooperative, batch, dealer, account, transaction, farmers, factory

router = APIRouter()

router.include_router(account.router)
router.include_router(user.router)
router.include_router(cooperative.router)
router.include_router(batch.router)
router.include_router(stock.router)
router.include_router(transaction.router)
router.include_router(factory.router)
router.include_router(dealer.router)
router.include_router(farmers.router)