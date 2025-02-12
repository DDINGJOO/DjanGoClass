import requests
import base64
import os
from django.shortcuts import render, resolve_url
from django.http import JsonResponse
from rest_framework.views import APIView


def pokedex_view(request, numbers): # URL에서 받은 번호 목록을 리스트로 변환
    pokemons = []

    for number in range(1, int(numbers) + 1):

        # 포켓몬 기본 정보 가져오기
        pokedex_url = f"http://127.0.0.1:8000/api/pokedex/get/number/{number}"
        response = requests.get(pokedex_url)

        if response.status_code != 200:
            continue  # API 응답 실패하면 건너뛰기

        try:
            pokedex_response = response.json()
        except requests.exceptions.JSONDecodeError:
            continue  # JSON 파싱 실패하면 건너뛰기

        # 포켓몬 이미지 가져오기
        image_url = f"http://127.0.0.1:8000/api/pokedeximage/get/number/{number}"
        image_response = requests.get(image_url)

        image_base64 = ""
        if image_response.status_code == 200:
            try:
                image_data = image_response.json()
                image_path = image_data.get("image", "")

                # ✅ 로컬 파일을 직접 읽어 Base64 변환
                if os.path.exists(image_path):
                    with open(image_path, "rb") as image_file:
                        image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
            except requests.exceptions.JSONDecodeError:
                pass  # 이미지 변환 실패 시 빈 값 유지

        # 포켓몬 데이터 저장
        pokemon_data = {
            "name": pokedex_response.get("name", "Unknown"),
            "id": pokedex_response.get("id", 0),
            "hp": pokedex_response.get("hp", 0),
            "attack": pokedex_response.get("attack", 0),
            "defense": pokedex_response.get("defense", 0),
            "image_base64": image_base64,  # Base64 인코딩된 이미지
        }
        pokemons.append(pokemon_data)

    return render(request, "pokedex.html", {"pokemons": pokemons})



class PokedexInitView(APIView):
    def get(self,request):
        initStats = f"http://127.0.0.1:8000/api/pokedex/post/number/152"
        requests.get(initStats)
        for i in range(1, 152):
            initImages = f"http://127.0.0.1:8000/api/pokedeximage/post/number/{i}"
            requests.get(initImages)