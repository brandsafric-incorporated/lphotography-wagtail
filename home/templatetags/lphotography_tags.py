from django import template

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object comparison to self will return false as objects would differ
    return context['request'].site.root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


@register.inclusion_tag('home/tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menu_items = parent.get_children().live().in_menu()

    for menu_item in menu_items:
        menu_item.show_dropdown = has_menu_children(menu_item)

        # We don't just check if calling_page is None as the template engine can pass an empty string as calling_page
        # if the variable passed as calling_page does not exist. Hence why we check the URL.
        menu_item.active = (calling_page.url.startswith(menu_item.url) if calling_page else False)

    return {
        'calling_page': calling_page,
        'parent': parent,
        'menu_items': menu_items,
        # Required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag('home/tags/top_menu_children.html', takes_context=True)
def top_menu_childen(context, parent):
    menu_items_children = parent.get_children()
    menu_items_children = menu_items_children.live().in_menu()

    return {
        'parent': parent,
        'menu_items_children': menu_items_children,
        # Required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag('home/tags/standard_index_listing.html', takes_context=True)
def standard_index_listing(context, calling_page):
    pages = calling_page.get_children().live()

    return {
        'pages': pages,
        # Required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }
