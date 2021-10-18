from django.shortcuts import render
from django.shortcuts import render
import Camps

from Camps.models import CampModel, Conformation, aboutModel, instaLinkModel, youTubeModel
def home(request):
    camps = CampModel.objects.filter(camp_latest=True)
    insta = instaLinkModel.objects.all()
    youtube=youTubeModel.objects.all()
    return render(request,'index.html', {'camps': camps,'insta':insta,'youtube':youtube})

def camps(request):
    camps = CampModel.objects.filter(camp_latest=True)
    return render(request,'camp-info.html',{'camps': camps})

def contact(request):
    return render(request,'contact.html')

def about(request):
    about = aboutModel.objects.filter(about_latest=True)
    return render(request,'about.html',{'about':about})

def makelist(obj):
    lt = obj.split(";")
    ans = []
    for i in lt:
        i = i.replace('\r\n', "")
        if ',' in i:
            slt = i.split(',')
            ans.append(slt)
        else:
            ans.append(i)
    return ans

def registrationForm(request):
    if request.method == "POST":
        title = request.POST.get('camptitle')
        camp = CampModel.objects.filter(title=title)
        package = makelist(camp[0].camp_packages)
        camp_dates = makelist(camp[0].camp_dates)
        return render(request, 'registration-form.html', {'camp': camp, 'package': package, 'date': camp_dates})

def camp_info(request, title):
    camp = CampModel.objects.filter(title=title)
   
    package = makelist(camp[0].camp_packages)
    camp_dates = makelist(camp[0].camp_dates)
    schedule = makelist(camp[0].camp_schedules)
    place = makelist(camp[0].camp_places_to_visit)
    activity = makelist(camp[0].camp_activities)
    inclusion = makelist(camp[0].camp_inclusions)
    exclusion = makelist(camp[0].camp_exclusions)
    carried_thing = makelist(camp[0].camp_carried_things)
    guideline = makelist(camp[0].camp_guidelines)
    instruction = makelist(camp[0].camp_instructions)
    return render(request, 'campInformation.html',
                  {'camp': camp, 'package': package, 'date': camp_dates, 'schedule': schedule, 'place': place,
                   'activity': activity, 'inclusion': inclusion, 'exclusion': exclusion, 'carried_thing': carried_thing,
                   'guideline': guideline, 'instruction': instruction})

def campConformation(request):
    if request.method == "POST":
        camp_title = request.POST.get('camp')
        camp_package = request.POST.get('pack')
        camp_date = request.POST.get('date')
        camp_rate = request.POST.get('Rate')
        camp_name = request.POST.get('name')
        camp_email = request.POST.get('email')
        camp_mobile = request.POST.get('mobile')
        camp_address = request.POST.get('address')
        camp_id_proof = request.FILES['id_proof']
        camp_photo = request.FILES['photo']
        camp_bdate = request.POST.get('bdate')
        camp_gender = request.POST.get('gender')
        camp_blood_group = request.POST.get('blood_group')
        camp_weight = request.POST.get('weight')
        camp_occupation = request.POST.get('occupation')
        camp_organization = request.POST.get('organization', "")
        camp_guardian_name = request.POST.get('guardian_name')
        camp_guardian_email = request.POST.get('guardian_email')
        camp_guardian_mobile = request.POST.get('guardian_mobile')
        camp_participated_where = request.POST.get('participated_where')
        camp_disease_phobia = request.POST.get('disease_phobia')
        camp_reference = request.POST.get('reference')
        camp_online_name = request.POST.get('online_name')
        camp_online_email = request.POST.get('online_email')
        camp_online_mobile = request.POST.get('online_mobile')

        book, created = Conformation.objects.get_or_create(title=camp_title, package=camp_package, date=camp_date, rate=camp_rate, name=camp_name,
                                                   email=camp_email, mobile=camp_mobile, address=camp_address, id_proof=camp_id_proof,
                                                   photo=camp_photo, bdate=camp_bdate, gender=camp_gender, blood_group=camp_blood_group,
                                                   weight=camp_weight, occupation=camp_occupation, organization=camp_organization,
                                                   guardian_name=camp_guardian_name, guardian_email=camp_guardian_email,
                                                   guardian_mobile=camp_guardian_mobile,
                                                   participated_where=camp_participated_where, disease_phobia=camp_disease_phobia,
                                                   reference=camp_reference, online_name=camp_online_name,
                                                   online_email=camp_online_email, online_mobile=camp_online_mobile)
        book.save()
        return render(request, 'confirmation.html')