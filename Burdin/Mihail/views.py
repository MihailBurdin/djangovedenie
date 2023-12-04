from django.http import HttpResponse

def index(request,name,age,interes):
    return HttpResponse(f"""
                <h2>О пользователе<h2>
                <p>Имя:{name} </p>
                <p>Возраст:{age} </p>
                <p>Интересы:{interes}<p>
""")

def about(request,arrived,grade,like_stude):
    return HttpResponse(f"""
            <h2>Информация о себе<h2>
            <p>Откуда приехала:{arrived}</p>
            <p>Успеваемость в школе:{grade}</p>
            <p>любите/не любите учиться:{like_stude}</p>
""")
def contact(requect,telephone):
    return HttpResponse(f"""
            <h2>Информация о себе<h2>
            <p>Мобильный телефон:{telephone}</p>                      
""")

