from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from apps.base.schemas import URL, PaymentServiceInfo


@dataclass(kw_only=True)
class CommissionCalculationInfo(PaymentServiceInfo):
    payment_amount: Decimal


@dataclass(kw_only=True)
class BalanceIncreaseData(CommissionCalculationInfo):
    user_uuid: UUID
    return_url: URL


@dataclass(kw_only=True)
class YookassaRequestPayment(BalanceIncreaseData):
    metadata: dict