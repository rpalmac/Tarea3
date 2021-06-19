{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled39.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOTg9YJIfyZheZ0IRUzQvCY",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Tarea3/blob/main/Ejercicio7.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "N_yiH29gGbZH"
      },
      "source": [
        "import pandas as pd\n",
        "\n",
        "# Generar un DataFrame con los datos del fichero.\n",
        "titanic = pd.read_csv('https://github.com/rpalmac/Tarea3/blob/main/titanic.csv', index_col=0)\n",
        "\n",
        "print(titanic)\n",
        "\n",
        "# Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas.\n",
        "print('Dimensiones:', titanic.shape)\n",
        "print('Número de elemntos:', titanic.size)\n",
        "print('Nombres de columnas:', titanic.columns)\n",
        "print('Nombres de filas:', titanic.index)\n",
        "print('Tipos de datos:\\n', titanic.dtypes)\n",
        "print('Primeras 10 filas:\\n', titanic.head(10))\n",
        "print('Últimas 10 filas:\\n', titanic.tail(10))\n",
        "\n",
        "# Mostrar por pantalla los datos del pasajero con identificador 148\n",
        "print(titanic.loc[148])\n",
        "\n",
        "# Mostrar por pantalla las filas pares del DataFrame.\n",
        "print(titanic.iloc[range(0,titanic.shape[0],2)])\n",
        "\n",
        "# Mostrar los nombres de las personas que iban en primera clase ordenadas alfabéticamente.\n",
        "print(titanic[titanic[\"Pclass\"]==1]['Name'].sort_values())\n",
        "\n",
        "# Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron\n",
        "print(titanic['Survived'].value_counts()/titanic['Survived'].count() * 100)\n",
        "\n",
        "# Alternativa\n",
        "print(titanic['Survived'].value_counts(normalize=True) * 100)\n",
        "\n",
        "#Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase\n",
        "print(titanic.groupby('Pclass')['Survived'].value_counts(normalize=True))\n",
        "\n",
        "# Eliminar del DataFrame los pasajeros con edad desconocida.\n",
        "titanic.dropna(subset=['Age'])\n",
        "\n",
        "# Alternativa \n",
        "# titanic = titanic[titanic['Age'].notna()]\n",
        "\n",
        "# Mostrar la edad media de las mujeres que viajaban en cada clase.\n",
        "print(titanic.groupby(['Pclass','Sex'])['Age'].mean().unstack()['female'])\n",
        "\n",
        "# Mostrar el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.\n",
        "print(titanic.groupby(['Pclass', 'Young'])['Survived'].value_counts(normalize = True) * 100)\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}