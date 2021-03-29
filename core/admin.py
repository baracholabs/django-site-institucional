from django.contrib import admin

from .models import Service, TeamRole, TeamMember


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("service", "icone", "description", "ativo")


@admin.register(TeamRole)
class TeamRoleAdmin(admin.ModelAdmin):
    list_display = ("role", "ativo")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "team_role", "ativo")
