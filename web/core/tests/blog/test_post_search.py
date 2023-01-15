import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark =pytest.mark.django_db

class TestListbysearch:
    def test_search_url(self, client):
        url = reverse("post_search")
        response = client.get(url)
        assert response.status_code==200

    def test_search_htmx_fragment(self, client, post_factory):
        headers = {"HTTP_HX-Request": "true"}
        url = reverse("post_search")
        response = client.get(url, **headers)
        assertTemplateUsed(response, "blog/components/post-list-elements-search.html")

    def test_search_filter(self, client, post_factory):
        post =  post_factory(title="test_post", tags=["test-tag"])
        url = reverse("post_search")
        request = f"{url}?q={post.title}"
        response =  client.get(request)
        assert post.title in response.context["posts"][0].title
        #The assertion bellow does the same thing as the above, the only difference is that it's looking for throughout the page.
        assert post.title in response.content.decode("utf-8")