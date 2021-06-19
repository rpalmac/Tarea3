{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled36.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPI88ENZPQNiJ9leUhQMjJj",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Tarea3/blob/main/Ejercicio3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "W26SpyEjErOf",
        "outputId": "876e0d83-1344-4533-c79e-802ea0e9af26",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "import pandas as pd\n",
        "\n",
        "def aprobados(notas):\n",
        "    notas = pd.Series(notas)\n",
        "    return notas[notas >= 5].sort_values(ascending=False)\n",
        "\n",
        "notas = {'Raul':9, 'Allan':6.5, 'Azael':4, 'Armando': 8.5, 'Angel': 5}\n",
        "print(aprobados(notas))"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Raul       9.0\n",
            "Armando    8.5\n",
            "Allan      6.5\n",
            "Angel      5.0\n",
            "dtype: float64\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}