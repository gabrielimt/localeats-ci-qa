Feature: Cálculo do valor total do pedido
  Como um cliente do LocalEats
  Eu quero que o sistema calcule a soma dos itens do meu pedido
  Para que eu saiba o valor exato que devo pagar

  Scenario: Soma exata dos itens do pedido
    Given que eu adicionei itens com os valores 10, 20 e 30 ao pedido
    When o sistema calcula o valor total
    Then o resultado retornado deve ser 60