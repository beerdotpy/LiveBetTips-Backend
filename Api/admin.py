from django.contrib import admin
from Api.models import User,Team,LeagueType,League,Prediction,Unit,CompletedText,PredictionDetail,PurchasedPrediction,tempUser,Profile	


class PredictionDetailAdmin(admin.ModelAdmin):
     
     list_display = ('id','leagueType','homeTeam','awayTeam','isPushNotifSend','isCompleted','isTipVerified')
     list_filter =  ['isCompleted']

#class UserAdmin(admin.ModelAdmin):
#     list_display = ('id','email','password','DateTimeVerified')

class LeagueAdmin(admin.ModelAdmin):
     list_display = ('name','countryFlagUrl')

class PredictionAdmin(admin.ModelAdmin):
     list_display = ('id','name','message')

class PurchasedPredictionAdmin(admin.ModelAdmin):
     list_display = ('id','userID','predictionID')

#admin.site.register(User,UserAdmin)
admin.site.register(Team)
admin.site.register(LeagueType)
admin.site.register(League,LeagueAdmin)
admin.site.register(Prediction,PredictionAdmin)
admin.site.register(Unit)
admin.site.register(CompletedText)
admin.site.register(PredictionDetail,PredictionDetailAdmin)
admin.site.register(PurchasedPrediction,PurchasedPredictionAdmin)
#admin.site.register(tempUser)
#admin.site.register(Profile)



# Register your models here.
