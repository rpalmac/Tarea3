{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled37.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPutxSJQWjwjCM9LDG7rbz8",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Tarea3/blob/main/Ejercicio4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uDRYlxw_FLPp"
      },
      "source": [
        "import pandas as pd\n",
        "\n",
        "datos = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 'Ventas':[30500, 35600, 28300, 33900], 'Gastos':[22000, 23400, 18100, 20700]}\n",
        "contabilidad = pd.DataFrame(datos)\n",
        "print(contabilidad)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}