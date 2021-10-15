# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .service.cidades_atendimento_service import listar_diaristas_cidade
from .serializer import diaristas_cidade_serializer
# Create your views here.


class DiaristasCidadeList(APIView):
    def get(self, request, format=None):
        cep = self.request.query_params.get('cep, None')
        diaristas = listar_diaristas_cidade(cep)
        serializer = diaristas_cidade_serializer.DiaristaCidadeSerializer(diaristas, many=True,
                                                                          context={"request": request})
        return Response(serializer.data)
