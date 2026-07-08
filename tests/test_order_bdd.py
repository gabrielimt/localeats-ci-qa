# tests/test_order_bdd.py
from pytest_bdd import scenarios, given, when, then, parsers
from order import calculate_total

# Aponta para o arquivo .feature que criamos
scenarios('features/order_total.feature')

# Fixture que prepara os dados (Given)
@given(parsers.parse('que eu adicionei itens com os valores {val1:d}, {val2:d} e {val3:d} ao pedido'), target_fixture='items')
def order_items(val1, val2, val3):
    return [val1, val2, val3]

# Ação que executa a funcionalidade (When)
@when('o sistema calcula o valor total', target_fixture='total')
def calculate(items):
    return calculate_total(items)

# Validação do resultado (Then)
@then(parsers.parse('o resultado retornado deve ser {expected_total:d}'))
def verify_total(total, expected_total):
    assert total == expected_total