import random

from django.shortcuts import render

# Create your views here.

def dashboard(request):
    # Page from the theme
    return render(request, 'pages/dashboard.html')

def courses(request):
    # Page from the theme
    return render(request, 'pages/courses.html')

def testing(request):

    questions = [
        {
            'id': 1,
            'question': '''1. Производная функции \(f(x) = 3x^2 + 2x\) по переменной \(x\):\(f'(x) = 6x + 2\)''',
            'answers': [
                '''6x+2''',
                '6x-2',
                '3x+2',
                '3x-2'
            ],
            'solution': """<ol>
        <li>Записываем функцию: \(f(x) = 3x^2 + 2x\)</li>
        <li>Применяем правило дифференцирования степенной функции: \(f'(x) = 2 \cdot 3x^{2-1} + 1 \cdot 2x^{1-1}\)</li>
        <li>Упрощаем выражение: \(f'(x) = 6x + 2\)</li>
    </ol>
    <p>Ответ: \(f'(x) = 6x + 2\)</p>"""
        },
        {
            'id': 2,
            'question': '''2. Площадь фигуры, ограниченной графиками функций \(f(x) = \sqrt{x}\) и \(g(x) = x^2\) на отрезке \([0, 1]\)''',
            'answers': [
                '''\(\\frac{1}{3}\)''',
                '''\(\\frac{1}{2}\)''',
                '''\(\\frac{2}{3}\)''',
                '''\(\\frac{3}{4}\)'''
            ],
            'solution': """<ol>
        <li>Находим точки пересечения графиков функций: \(f(x) = g(x)\)</li>
        <ul>
            <li>\(\sqrt{x} = x^2\)</li>
            <li>\(x^2 - \sqrt{x} = 0\)</li>
        </ul>
        <li>Решаем уравнение: \(x^2 - \sqrt{x} = 0\)</li>
        <ul>
            <li>Корни уравнения: \(x = 0, x = 1\)</li>
        </ul>
        <li>Вычисляем площадь между графиками функций на отрезке \([0, 1]\)</li>
        <ul>
            <li>Площадь = \(\int_0^1 (g(x) - f(x)) \,dx\)</li>
            <li>Площадь = \(\int_0^1 (x^2 - \sqrt{x}) \,dx\)</li>
            <li>Площадь = \(\left[\\frac{x^3}{3} - \\frac{2}{3}x^{\\frac{3}{2}}\\right]_0^1\)</li>
            <li>Площадь = \(\\frac{1}{3} - \\frac{2}{3} = \\frac{1}{3}\)</li>
        </ul>
    </ol>
    <p>Ответ: Площадь = \(\\frac{1}{3}\)</p>"""
        },
        {
            'id': 3,
            'question': '''3. Интеграл, представляющий площадь фигуры, ограниченной графиками функций \(f(x) = \sin(x)\) и \(g(x) = \cos(x)\) на интервале \([0, \pi]\)''',
            'answers': [
                '''\(\int_0^{\pi} (\cos(x) - \sin(x)) \,dx\)''',
                '''\(\int_0^{\pi} (\sin(x) - \cos(x)) \,dx\)''',
                '''\(\int_0^{\pi} (\sin(x) + \cos(x)) \,dx\)''',
                '''\(\int_0^{\pi} (\cos(x) + \sin(x)) \,dx\)'''
            ],
            'solution': """<ol>
        <li>Вычисляем точки пересечения графиков функций: \(f(x) = g(x)\)</li>
        <ul>
            <li>\(\sin(x) = \cos(x)\)</li>
        </ul>
        <li>Находим точки пересечения графиков функций:</li>
        <ul>
            <li>\(\sin(x) = \cos(x)\)</li>
            <li>\(\\tan(x) = 1\)</li>
        </ul>
        <li>Решаем уравнение: \(\\tan(x) = 1\)</li>
        <ul>
            <li>Решение уравнения: \(x = \\frac{\pi}{4}\)</li>
        </ul>
        <li>Вычисляем площадь между графиками функций на интервале \([0, \pi]\)</li>
        <ul>
            <li>Площадь = \(\int_0^\\frac{\pi}{4} (\cos(x) - \sin(x)) \,dx\)</li>
            <li>Площадь = \(\left[\sin(x) + \cos(x)\\right]_0^\\frac{\pi}{4}\)</li>
            <li>Площадь = \(\sin\left(\\frac{\pi}{4}\\right) + \cos\left(\\frac{\pi}{4}\\right) - (\sin(0) + \cos(0))\)</li>
            <li>Площадь = \(\sqrt{2} - (1 + 1) = \sqrt{2} - 2\)</li>
        </ul>
    </ol>
    <p>Ответ: Площадь = \(\sqrt{2} - 2\)</p>"""
        },
        {
            'id': 4,
            'question': '''4. Корни уравнения \(x^3 - 5x^2 + 6x = 0\)''',
            'answers': [
                '0,2',
                '0,3',
                '1,2',
                '1,3'
            ],
            'solution': """ <ol>
        <li>Факторизуем уравнение:</li>
        <ul>
            <li>\(x(x^2 - 5x + 6) = 0\)</li>
        </ul>
        <li>Находим корни каждого множителя отдельно:</li>
        <ul>
            <li>Первый множитель: \(x = 0\)</li>
            <li>Второй множитель: \(x^2 - 5x + 6 = 0\)</li>
        </ul>
        <li>Решаем квадратное уравнение:</li>
        <ul>
            <li>\(x^2 - 5x + 6 = 0\)</li>
            <li>\((x - 2)(x - 3) = 0\)</li>
        </ul>
        <li>Таким образом, получаем следующие корни:</li>
        <ul>
            <li>\(x = 0\)</li>
            <li>\(x = 2\)</li>
            <li>\(x = 3\)</li>
        </ul>
    </ol>
    <p>Ответ: Корни уравнения \(x^3 - 5x^2 + 6x = 0\) равны \(x = 0\), \(x = 2\) и \(x = 3\).</p>"""
        },
        {
            'id': 5,
            'question': '''5. Значение предела \(\lim_{{x \\to \infty}} \\frac{{e^x}}{{x^2}}\)''',
            'answers': [
                '\(\infty\)',
                '0',
                '1',
                'не существует'
            ],
            'solution': """<ol>
        <li>Применим правило Лопиталя:</li>
        <ul>
            <li>\(\lim_{{x \\to \infty}} \\frac{{e^x}}{{x^2}} = \lim_{{x \\to \infty}} \\frac{{(e^x)'}}{{(x^2)'}}\)</li>
            <li>\(\lim_{{x \\to \infty}} \\frac{{e^x}}{{x^2}} = \lim_{{x \\to \infty}} \\frac{{e^x}}{{2x}}\)</li>
        </ul>
        <li>Применим правило Лопиталя ещё раз:</li>
        <ul>
            <li>\(\lim_{{x \\to \infty}} \\frac{{e^x}}{{2x}} = \lim_{{x \\to \infty}} \\frac{{(e^x)'}}{{(2x)'}}\)</li>
            <li>\(\lim_{{x \\to \infty}} \\frac{{e^x}}{{2x}} = \lim_{{x \\to \infty}} \\frac{{e^x}}{{2}}\)</li>
        </ul>
        <li>Так как \(e^x\) растёт экспоненциально, а \(2x\) линейно, то предел равен:</li>
        <ul>
            <li>\(\lim_{{x \\to \infty}} \\frac{{e^x}}{{2}} = +\infty\)</li>
        </ul>
    </ol>
    <p>Ответ: Значение предела \(\lim_{{x \\to \infty}} \\frac{{e^x}}{{x^2}}\) равно \(+\infty\).</p>"""
        },
    ]



    if request.method == "POST":
        incorrect_list = []
        score = 0
        print(request.POST)
        for q in questions:
            if str(q['id']) in request.POST:
                if request.POST[str(q['id'])] == q['answers'][0]:
                    score += 1
                else:
                    incorrect_list.append(q['id'])
            else:
                incorrect_list.append(q['id'])

        incorrect_questions = []
        for id in incorrect_list:
            for q in questions:
                if q['id'] == id:
                    incorrect_questions.append({
                        'id': id,
                        'question': q['question'],
                        'answer': request.POST[str(q['id'])] if str(q['id']) in request.POST else 'Без ответа',
                        'correct_answer': q['answers'][0],
                        'solution': q['solution']
                    })

        return render(request, 'pages/result.html', context={'score': score, 'max_score': len(questions), 'inccorect': incorrect_questions })

    for q in questions:
        random.shuffle(q['answers'])
    theme = 'Интегралы'
    return render(request, 'pages/testing.html', context={'context': questions, 'theme': theme})
