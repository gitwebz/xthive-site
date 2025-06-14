from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Service, PortfolioItem, BlogPost, JobOpening, Client, Testimonial, TeamMember, CaseStudy, ContactMessage
from .forms import ContactForm

def home(request):
    services = Service.objects.all()[:6]
    portfolio_items = PortfolioItem.objects.all()[:6]
    testimonials = Testimonial.objects.all()[:3]
    clients = Client.objects.all()[:8]
    return render(request, 'home.html', {
        'services': services,
        'portfolio_items': portfolio_items,
        'testimonials': testimonials,
        'clients': clients,
    })

def about(request):
    team_members = TeamMember.objects.all()
    return render(request, 'about.html', {'team_members': team_members})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def portfolio(request):
    projects = PortfolioItem.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

def portfolio_detail(request, slug):
    project = get_object_or_404(PortfolioItem, slug=slug)
    return render(request, 'portfolio_detail.html', {'project': project})

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_detail.html', {'post': post})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            send_mail(
                f"New Contact Message from {contact_message.name}",
                contact_message.message,
                contact_message.email,
                ['info@xthive.com'],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def careers(request):
    jobs = JobOpening.objects.all()
    return render(request, 'careers.html', {'jobs': jobs})

def case_studies(request):
    case_studies = CaseStudy.objects.all()
    return render(request, 'case_studies.html', {'case_studies': case_studies})

def case_study_detail(request, slug):
    case_study = get_object_or_404(CaseStudy, slug=slug)
    return render(request, 'case_study_detail.html', {'case_study': case_study})

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials.html', {'testimonials': testimonials})

def pricing(request):
    return render(request, 'pricing.html')