from django.contrib import admin
from .models import Service, PortfolioItem, BlogPost, JobOpening, Client, Testimonial, TeamMember, CaseStudy, ContactMessage

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'created_at')
    search_fields = ('title', 'description', 'technologies')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content', 'tags')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_type', 'posted_at')
    search_fields = ('title', 'description')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'rating', 'created_at')
    search_fields = ('client_name', 'message')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'created_at')
    search_fields = ('name', 'position')

@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'created_at')
    search_fields = ('title', 'overview', 'challenge', 'solution')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')