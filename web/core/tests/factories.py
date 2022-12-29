import factory
from core.blog.models import Post
from django.contrib.auth.models import User
from factory.faker import faker

FAKE = faker.Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    password = "test"
    username = "test"
    is_superuser = True
    is_staff = True
    is_active = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=12)
    subtitle = factory.Faker("sentence", nb_words=12)
    slug = factory.Faker("slug")
    author = factory.SubFactory(UserFactory)
    status = "published"

    @factory.lazy_attribute
    def content(self):
        conteudo = ""
        for _ in range(0, 5):
            conteudo += "\n" + FAKE.paragraph(nb_sentences=30) + "\n"

        return conteudo

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.tags.add(*extracted)
