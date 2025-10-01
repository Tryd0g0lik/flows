"""
admins/filters.py
"""

from django.contrib.admin import SimpleListFilter


class TitleFilter(SimpleListFilter):
    title = "Заголовок начинается с:"
    parameter_name = "title_start"

    def lookups(self, request, model_admin):
        return [
            ("a", "A"),
            ("b", "B"),
            ("c", "C"),
            ("d", "D"),
            ("e", "E"),
            ("f", "F"),
            ("g", "G"),
            ("h", "H"),
            ("i", "I"),
            ("j", "J"),
            ("k", "K"),
            ("l", "L"),
            ("m", "M"),
            ("n", "N"),
            ("o", "O"),
            ("p", "P"),
            ("q", "Q"),
            ("r", "R"),
            ("s", "S"),
            ("t", "T"),
            ("v", "V"),
            ("w", "W"),
            ("x", "X"),
            ("y", "Y"),
            ("z", "Z"),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(name__icontains=self.value())
        return queryset
