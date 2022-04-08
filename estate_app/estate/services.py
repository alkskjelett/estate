HOUSE_TYPES = (
    (1, 'Панельный'),
    (2, 'Кирпичный'),
    (3, 'Монолитный')
)

HEATING_TYPES = (
    (1, 'Отопление тёплыми полами'),
    (2, 'Водяное'),
    (3, 'Воздушное'),
    (4, 'Паровое'),
)

announcementFilterFields = {
    'cost': ['gt', 'lt'],
    'address': ['exact'],
    'filters__fridge': ['exact'],
    'filters__microwave': ['exact'],
    'filters__washMachine': ['exact'],
    'filters__oven': ['exact'],
    'filters__conditioner': ['exact'],
    'filters__router': ['exact'],
    'filters__TV': ['exact'],
}

def user_directory_path(instance, filename):
    return 'media/user_{0}/{1}'.format(instance.user.id, filename)

def announcement_directory_path(instance, filename):
    return 'media/announcement_{0}/{1}'.format(instance.announcement.id, filename)

