from datetime import datetime

class Stock:
    def __init__(self, name, prices):
        """
        Inicializa un stock con un nombre y un diccionario de precios históricos.
        :param name: Nombre del stock
        :param prices: Diccionario con fechas (datetime) como clave y precios (float) como valor
        """
        self.name = name
        self.prices = prices

    def price(self, date):
        """
        Retorna el precio del stock en una fecha específica.
        :param date: Fecha en formato datetime
        :return: Precio en la fecha dada, o None si no hay precio disponible
        """
        return self.prices.get(date)


class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        """
        Agrega stock al protafolio
        """
        self.stocks.append(stock)

    def profit(self, start_date, end_date):
        """
        Calcula la ganancia total del portafolio entre dos dates
        """
        total_start = sum(stock.price(start_date) for stock in self.stocks if stock.price(start_date) is not None)
        total_end = sum(stock.price(end_date) for stock in self.stocks if stock.price(end_date) is not None)

        if total_start == 0:
            return 0  # edge case al div por 0

        return total_end - total_start

    def annualized_return(self, start_date, end_date):
        """
        Calcula el retorno anualizado del portafolio entre dos fechas.
        """
        profit = self.profit(start_date, end_date)
        total_start = sum(stock.price(start_date) for stock in self.stocks if stock.price(start_date) is not None)

        if total_start == 0:
            return 0 

        days = (end_date - start_date).days
        if days <= 0:
            return 0

        # Calculo del retorno anualizado
        annualized_return = (1 + (profit / total_start)) ** (365 / days) - 1
        return annualized_return * 100


# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de precios de un stock
    stock_a = Stock("Completos", {
        datetime(2024, 1, 1): 100.0,
        datetime(2024, 12, 31): 120.0,
    })

    stock_b = Stock("Chorrillanas", {
        datetime(2024, 1, 1): 50.0,
        datetime(2024, 12, 31): 55.0,
    })

    # Creación del portafolio y stock
    portfolio = Portfolio()
    portfolio.add_stock(stock_a)
    portfolio.add_stock(stock_b)

    # Calculos
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)

    print(f"Ganancia entre las fechas: {portfolio.profit(start_date, end_date)}")
    print(f"Retorno anualizado: {portfolio.annualized_return(start_date, end_date):.2f}%")
