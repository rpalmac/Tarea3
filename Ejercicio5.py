{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled38.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMEhNB2zJ+ZvoZPxIZSY7bl",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Tarea3/blob/main/Ejercicio5.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "o-ygyQ0LFm6D",
        "outputId": "3c9f83fc-5d55-4a89-ad25-61c6aced728d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "import pandas as pd\n",
        "\n",
        "datos = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 'Ventas':[30500, 35600, 28300, 33900], 'Gastos':[22000, 23400, 18100, 20700]}\n",
        "\n",
        "contabilidad = pd.DataFrame(datos)\n",
        "\n",
        "def balance(contabilidad, meses):\n",
        "    contabilidad['Balance'] = contabilidad.Ventas - contabilidad.Gastos\n",
        "    return contabilidad[contabilidad.Mes.isin(meses)].Balance.sum()\n",
        "\n",
        "print(balance(contabilidad, ['Enero','Marzo']))"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "18700\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}