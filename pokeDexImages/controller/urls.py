from django.urls import path
from pokeDexImages.controller.views import PokeDexImageView, PokeDexImageDeleteView, PokeDexImagePostView, \
    PokeDexImagesView

urlpatterns = [
    path("/get/number/<int:number>", PokeDexImageView.as_view()),  # GET 요청
    path("/post/number/<int:number>", PokeDexImagePostView.as_view()),  # POST 요청
    path("/delete/number/<int:number>", PokeDexImageDeleteView.as_view()),  # DELETE 요청
    path("/get/images", PokeDexImagesView.as_view()),
]


