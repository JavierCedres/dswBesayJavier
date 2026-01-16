import pytest

from factories import (
    CategoryFactory,
    GameFactory,
    OrderFactory,
    PlatformFactory,
    ReviewFactory,
    TokenFactory,
    UserFactory,
)

# ==============================================================================
# URL Patterns
# ==============================================================================

CATEGORY_LIST_URL = '/api/categories/'
CATEGORY_DETAIL_URL = '/api/categories/{category_slug}/'

GAME_LIST_URL = '/api/games/'
GAME_FILTER_URL = '/api/games/?category={category_slug}&platform={platform_slug}'
GAME_DETAIL_URL = '/api/games/{game_slug}/'

REVIEW_LIST_URL = '/api/games/{game_slug}/reviews/'
REVIEW_DETAIL_URL = '/api/games/reviews/{review_pk}/'
REVIEW_ADD_URL = '/api/games/{game_slug}/reviews/add/'

ORDER_ADD_URL = '/api/orders/add/'
ORDER_DETAIL_URL = '/api/orders/{order_pk}/'
ORDER_GAME_LIST_URL = '/api/orders/{order_pk}/games/'
ORDER_ADD_GAME_URL = '/api/orders/{order_pk}/games/add/'
ORDER_STATUS_URL = '/api/orders/{order_pk}/status/'
ORDER_PAY_URL = '/api/orders/{order_pk}/pay/'

PLATFORM_LIST_URL = '/api/platforms/'
PLATFORM_DETAIL_URL = '/api/platforms/{platform_slug}/'

AUTH_URL = '/api/auth/'


# ==============================================================================
# Fixtures
# ==============================================================================


@pytest.fixture(autouse=True)
def media_tmpdir(settings, tmp_path):
    settings.MEDIA_ROOT = tmp_path / 'media'


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def token(user):
    return TokenFactory(user=user)


@pytest.fixture
def order(user):
    return OrderFactory(user=user)


@pytest.fixture
def game():
    return GameFactory()


@pytest.fixture
def category():
    return CategoryFactory()


@pytest.fixture
def platform():
    return PlatformFactory()


@pytest.fixture
def review(user, game):
    return ReviewFactory(author=user, game=game)
