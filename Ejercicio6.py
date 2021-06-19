{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled38.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMPo48/0zwY4Zbfpuul3qRi",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Tarea3/blob/main/Ejercicio6.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DvVVN8k6F1tF"
      },
      "source": [
        "import pandas as pd\n",
        "\n",
        "def resumen_cotizaciones(fichero):\n",
        "    df = pd.read_csv(fichero, sep=';', decimal=',', thousands='.', index_col=0)\n",
        "    return pd.DataFrame([df.min(), df.max(), df.mean()], index=['Mínimo', 'Máximo', 'Media'])\n",
        "\n",
        "resumen_cotizaciones('cotizacion.csv')"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}