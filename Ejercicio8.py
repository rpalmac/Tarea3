{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled40.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOx9RBrjYbQ6qjreB3znqcJ",
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
        "<a href=\"https://colab.research.google.com/github/rpalmac/Tarea3/blob/main/Ejercicio8.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sIN7B3UuHAa2"
      },
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import datetime as dt\n",
        "\n",
        "# Generar un DataFrame con los datos de los cuatro ficheros\n",
        "import pandas as pd \n",
        "\n",
        "emisiones_2016 = pd.read_csv('emisiones-2016.csv', sep = ';')\n",
        "emisiones_2017 = pd.read_csv('emisiones-2017.csv', sep = ';')\n",
        "emisiones_2018 = pd.read_csv('emisiones-2018.csv', sep = ';')\n",
        "emisiones_2019 = pd.read_csv('emisiones-2019.csv', sep = ';')\n",
        "emisiones = pd.concat([emisiones_2016, emisiones_2017, emisiones_2018, emisiones_2019])\n",
        "emisiones\n",
        "\n",
        "# Filtrar las columnas del DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc. \n",
        "columnas = ['ESTACION', 'MAGNITUD', 'ANO', 'MES']\n",
        "columnas.extend([col for col in emisiones if col.startswith('D')])\n",
        "emisiones = emisiones[columnas]\n",
        "emisiones\n",
        "\n",
        "# Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los días aparezcan en una única columna.\n",
        "emisiones = emisiones.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')\n",
        "emisiones\n",
        "\n",
        "# Crear una nueva columna con las fechas a partir del año, mes y día\n",
        "# Primero eliminamos el caracter D del comienzo de la columna de los días\n",
        "emisiones['DIA'] = emisiones.DIA.str.strip('D')\n",
        "# Concatenamos las columnas del año, mes y día\n",
        "emisiones['FECHA'] = emisiones.ANO.apply(str) + '/' + emisiones.MES.apply(str) + '/' + emisiones.DIA.apply(str)\n",
        "# Convertimos la nueva columna al tipo fecha\n",
        "emisiones['FECHA'] = pd.to_datetime(emisiones.FECHA, format='%Y/%m/%d', infer_datetime_format=True, errors='coerce')\n",
        "emisiones\n",
        "\n",
        "# Eliminar las filas con fechas no válidas\n",
        "emisiones = emisiones.drop(emisiones[np.isnat(emisiones.FECHA)].index)\n",
        "# Ordenar el el dataframe por estación, magnitud y fecha\n",
        "emisiones.sort_values(['ESTACION', 'MAGNITUD', 'FECHA'])\n",
        "\n",
        "# Mostrar las estaciones disponibles\n",
        "print('Estaciones:', emisiones.ESTACION.unique())\n",
        "# Mostrar los contaminantes disponibles\n",
        "print('Contaminantes:', emisiones.MAGNITUD.unique())\n",
        "\n",
        "# Función que devuelve las emisiones de un contaminante dado en una estación y rango de fechas dado.\n",
        "def evolucion(estacion, contaminante, desde, hasta):\n",
        "    return emisiones[(emisiones.ESTACION == estacion) & (emisiones.MAGNITUD == contaminante) & (emisiones.FECHA >= desde) & (emisiones.FECHA <= hasta)].sort_values('FECHA').VALOR\n",
        "evolucion(56, 8, dt.datetime.strptime('2018/10/25', '%Y/%m/%d'), dt.datetime.strptime('2019/02/12', '%Y/%m/%d'))\n",
        "\n",
        "# Resumen descriptivo por contaminantes\n",
        "emisiones.groupby('MAGNITUD').VALOR.describe()\n",
        "\n",
        "# Resumen descriptivo por contaminantes y distritos\n",
        "emisiones.groupby(['ESTACION', 'MAGNITUD']).VALOR.describe()\n",
        "\n",
        "# Función que devuelve un resumen descriptivo de la emisiones en un contaminante dado en un estación dada\n",
        "def resumen(estacion, contaminante):\n",
        "    return emisiones[(emisiones.ESTACION == estacion) & (emisiones.MAGNITUD == contaminante)].VALOR.describe()\n",
        "\n",
        "# Resumen de Dióxido de Nitrógeno en Plaza Elíptica\n",
        "print('Resumen Dióxido de Nitrógeno en Plaza Elíptica:\\n', resumen(56, 8),'\\n', sep='')\n",
        "# Resumen de Dióxido de Nitrógeno en Plaza del Carmen\n",
        "print('Resumen Dióxido de Nitrógeno en Plaza del Carmen:\\n', resumen(35, 8), sep='')\n",
        "\n",
        "# Función que devuelve una serie con las emisiones medias mensuales de un contaminante y un mes año para todos las estaciones\n",
        "def evolucion_mensual(contaminante, año):\n",
        "    return emisiones[(emisiones.MAGNITUD == contaminante) & (emisiones.ANO == año)].groupby(['ESTACION', 'MES']).VALOR.mean().unstack('MES')\n",
        "\n",
        "# Evolución del dióxido de nitrógeno en 2019\n",
        "evolucion_mensual(8, 2019)\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}