import factory
from core.blog.models import Post
from django.contrib.auth.models import User
from factory.faker import faker

FAKE = faker.Faker()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=12)
    subtitle = factory.Faker("sentence", nb_words=12)
    slug = factory.Faker("slug")
    author = User.objects.get_or_create(username="admin")[0]

    @factory.lazy_attribute
    def content(self):
        conteudo = ""
        for _ in range(0, 5):
            conteudo += "\n" + FAKE.paragraph(nb_sentences=30) + "\n"

        return conteudo

    status = "published"
