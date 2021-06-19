{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled35.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPr9VkjlHHWQVhSpJOnq08X",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Tarea3/blob/main/Ejercicio2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oKaRQEhTEJc4"
      },
      "source": [
        "import pandas as pd\n",
        "\n",
        "def estadistica_notas(notas):\n",
        "    notas = pd.Series(notas)\n",
        "    estadisticos = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index=['Min', 'Max', 'Media', 'Desviación típica'])\n",
        "    return estadisticos\n",
        "\n",
        "notas = {'Raul':9, 'Allan':6.5, 'Azael':4, 'Armando': 8.5, 'Angel': 5}\n",
        "print(estadistica_notas(notas))\n",
        "\n",
        "\n",
        "import pandas as pd\n",
        "\n",
        "def estadistica_notas(notas):\n",
        "    notas = pd.Series(notas)\n",
        "    return notas.describe()\n",
        "\n",
        "notas = {'Raul':9, 'Allan':6.5, 'Azael':4, 'Armando': 8.5, 'Angel': 5}\n",
        "print(estadistica_notas(notas))"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}