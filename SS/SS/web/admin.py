from django.contrib import admin
from .models import Info, Education, Work, CompBTstudents, CompMTstudents, ContMTstudents, CompPhdstudents, ContPhdstudents, ContBTstudents, publications, students, recognitions, project

# Register your models here.

admin.site.register(Info)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(ContPhdstudents)
admin.site.register(CompPhdstudents)
admin.site.register(ContMTstudents)
admin.site.register(CompBTstudents)
admin.site.register(CompMTstudents)
admin.site.register(ContBTstudents)
admin.site.register(publications)
admin.site.register(students)
admin.site.register(recognitions)
admin.site.register(project)