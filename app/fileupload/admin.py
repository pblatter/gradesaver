from django.contrib import admin
from fileupload.models import test_files

class exam_Admin(admin.ModelAdmin):
    list_display = ("Name", "Jahrgang", "Fach", "Schwerpunkt", "Lehrperson", "Exam", "user")

    def user_info(self, obj):
        return obj.user

    def get_queryset(self, request):
        queryset = super(exam_Admin, self).get_queryset(request)
        queryset = queryset.order_by('Fach', 'Jahrgang')
        return queryset

admin.site.register(test_files, exam_Admin)

# Register your models here.
