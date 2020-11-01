import codecs
import json

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework.views import APIView

from parrot_control import models
from parrot_control.parrot_gateway import parrot as parrot_gateway
import parrot_control.serializers as serializers
from django.views.generic import TemplateView

front_static = TemplateView.as_view(template_name='index.html')


class ParrotCommandController(APIView):

    def __init__(self):
        self.query_set = models.ParrotCommand.objects.all()

    def get(self, request):
        parrot_0 = self.query_set.filter(parrot_0=True)
        p0_movement_rs = parrot_0.filter(tag="P_M").order_by("priority", "arg")
        p0_voice_rs = parrot_0.filter(tag="P_V").order_by("priority", "arg")

        parrot_1 = self.query_set.filter(parrot_1=True)
        p1_movement_rs = parrot_1.filter(tag="P_M").order_by("priority", "arg")
        p1_voice_rs = parrot_1.filter(tag="P_V").order_by("priority", "arg")

        commands = {
            "parrot_0": {
                "movement": serializers.ParrotCommandSerializer(instance=p0_movement_rs, many=True).data,
                "voice": serializers.ParrotCommandSerializer(instance=p0_voice_rs, many=True).data
            },
            "parrot_1": {
                "movement": serializers.ParrotCommandSerializer(instance=p1_movement_rs, many=True).data,
                "voice": serializers.ParrotCommandSerializer(instance=p1_voice_rs, many=True).data
            }
        }

        return HttpResponse(json.dumps(commands), status=200, content_type='application/json; charset=utf8')

    def post(self, request):
        parrot_id = request.query_params['parrot_id']
        cmd_id = request.query_params['cmd_id']
        command = self.query_set.get(pk=cmd_id)
        parrot_gateway.send_cmd(parrot_id, command)
        return HttpResponse("OK", status=200, content_type='application/json; charset=utf8')
