import unittest.mock as mock
from unittest.mock import Mock
import unittest
from src import dolartodayservice


@mock.patch("dolartodayservice.requests.get")
class DolarTodayServiceTest(unittest.TestCase):
    URL_SERVICE_CORRECTA = r"http://api.dolartoday.com/"
    def setUp(self):
        self.get_mock = None
        self.dolartodayservice = dolartodayservice.DolarTodayService()
    def set_good_get_mock(self,get_mock):
        data = {
            "_antibloqueo": {
                "mobile": "https://d3g1wacrlruyoe.cloudfront.net",
                "video": "https://www.youtube.com/embed/videoseries?list=PL6qOmJKmpQ8QMt20uG_dlh9-jzjcvZOxU&showinfo=0",
                "corto_alternativo": "https://goo.gl/2zem6e",
                "enable_iads": "0",
                "alternativo": "68747470733a2f2f636c6f75642d313432303330343632382d63616368652e63646e2d6d61782e636f6d",
                "resource_id": "24989 A"
            },
            "_labels": {
                "a": "PARALELO",
                "b": "IMPLICITO",
                "c": "SICAD 2",
                "d": "SICAD 1",
                "e": "CENCOEX"
            },
            "_timestamp": {
                "epoch": "1421022608",
                "fecha": "Enero 11, 2015 08:00 PM",
                "fecha_corta": "Ene 11, 2015",
                "fecha_nice": "Enero 11, 2015",
                "dia": "Domingo",
                "dia_corta": "Dom"
            },
            "USD": {
                "transferencia": 187.19,
                "efectivo": 96.15,
                "efectivo_real": 167.56,
                "promedio": 187.19,
                "promedio_real": 52.01,
                "cencoex": 6.30,
                "sicad1": 12.00,
                "sicad2": 52.01,
                "dolartoday": 187.19
            },
            "EUR": {
                "transferencia": 222.15,
                "efectivo": 114.11,
                "efectivo_real": 198.81,
                "promedio": 222.15,
                "promedio_real": 61.73,
                "cencoex": 7.48,
                "sicad1": 14.24,
                "sicad2": 61.73,
                "dolartoday": 222.15
            },
            "COL": {
                "compra": 13.50,
                "venta": 14
            },
            "GOLD": {
                "rate": 1224.78
            },
            "USDVEF": {
                "rate": 6.35
            },
            "USDCOL": {
                "rate": 2527.00,
                "ratecash": 2262.00,
                "ratetrm": 2406.71,
                "trmfactor": 0.05,
                "trmfactorcash": 0.06
            },
            "EURUSD": {
                "rate": 1.1868
            },
            "BCV": {
                "fecha": "1420691400",
                "fecha_nice": "Enero 8, 2015",
                "liquidez": "2.010.126.877",
                "reservas": "20.907.000"
            }
        }
        self.get_mock = get_mock
        response = Mock()
        response.json = Mock(return_value=data)
        self.get_mock.return_value = response
    def test_call_dolar_today(self,get_mock):
        self.set_good_get_mock(get_mock)
        self.dolartodayservice.url = self.URL_SERVICE_CORRECTA
        self.dolartodayservice.getJSON()
        # Assert DolarTodayService is called with URL correcta
        self.get_mock.assert_called_with(self.URL_SERVICE_CORRECTA)
        # Assert we get the JSON we were looking for
        self.assertEquals(self.dolartodayservice.getJSON(),
                self.get_mock().json())
