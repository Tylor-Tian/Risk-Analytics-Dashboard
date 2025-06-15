from fastapi import APIRouter

from ..data import SAMPLE_INDICATORS

router = APIRouter()


@router.get("/overview")
def metrics_overview():
    return {
        "indicator_count": len(SAMPLE_INDICATORS),
        "categories": sorted({ind.category for ind in SAMPLE_INDICATORS}),
    }


@router.get("/category-summary")
def category_summary():
    result = {}
    for ind in SAMPLE_INDICATORS:
        result.setdefault(ind.category, 0)
        result[ind.category] += 1
    return result
