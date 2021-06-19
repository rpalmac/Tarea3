{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled34.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNiboppuDO2pA2Js++Q7wFl",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rpalmac/Tarea3/blob/main/Ejercicio1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ayecxPLhDhSm"
      },
      "source": [
        "import pandas as pd\n",
        "\n",
        "inicio = int(input('Introduce el año inicial: '))\n",
        "fin = int(input('Introduce el año final: '))\n",
        "ventas = {}\n",
        "for i in range(inicio, fin+1):\n",
        "    ventas[i] = float(input('Introduce las ventas del año ' + str(i) +': '))\n",
        "ventas = pd.Series(ventas)\n",
        "print('Ventas\\n', ventas)\n",
        "print('Ventas con descuento\\n', ventas*0.9)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}