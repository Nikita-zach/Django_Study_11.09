from django.contrib import admin
from .models import Category, Dish, Gallery, Event, Stuff, Contact, Reservation, FooterItems

admin.site.register(FooterItems)

class DishInline(admin.TabularInline):
    model = Dish
    extra = 1
    show_change_link = True

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible', 'sort', 'created_at', 'updated_at')
    list_editable = ('is_visible', 'sort')
    list_filter = ('is_visible', 'created_at', 'updated_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    inlines = [DishInline]

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'weight', 'unit', 'is_visible', 'category', 'created_at', 'updated_at')
    list_editable = ('is_visible', 'price', 'weight', 'unit')
    list_filter = ('is_visible', 'category', 'created_at', 'updated_at')
    search_fields = ('name', 'ingredients')
    date_hierarchy = 'created_at'

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date_start', 'date_end', 'is_visible', 'created', 'updated')
    list_editable = ('is_visible', 'price', 'date_start', 'date_end')
    list_filter = ('is_visible', 'date_start', 'date_end', 'created', 'updated')
    search_fields = ('name',)
    date_hierarchy = 'date_start'

@admin.register(Stuff)
class StuffAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'is_visible', 'created', 'updated')
    list_editable = ('is_visible',)
    list_filter = ('is_visible', 'created', 'updated')
    search_fields = ('name', 'profession')
    date_hierarchy = 'created'

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('photo', 'is_visible', 'created', 'updated')
    list_editable = ('is_visible',)
    list_filter = ('is_visible', 'created', 'updated')
    date_hierarchy = 'created'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'is_visible', 'created_at', 'updated_at')
    list_editable = ('is_visible',)
    list_filter = ('is_visible', 'created_at', 'updated_at')
    search_fields = ('title',)
    date_hierarchy = 'created_at'

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date', 'time', 'people', 'is_processed', 'created_at', 'updated_at')
    list_editable = ('is_processed',)
    list_filter = ('is_processed', 'date', 'created_at', 'updated_at')
    search_fields = ('name', 'phone', 'email')
    date_hierarchy = 'date'
