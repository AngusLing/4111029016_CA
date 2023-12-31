{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMgS3gRqL/36H0NuRhUdDJF",
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
        "<a href=\"https://colab.research.google.com/github/AngusLing/4111029016_CA/blob/main/week4.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "Ul1kJnu1MU5N",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "26c4038e-3fdc-4387-9405-9d9b9e2f3e0e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The column:\n",
            "(1, 'chicken', 30, 5)\n",
            "(2, 'beaf', 55, 10)\n",
            "(3, 'pork', 40, 15)\n",
            "The column:\n",
            "(1, 'chicken', 30, 30)\n",
            "(2, 'beaf', 55, 10)\n",
            "(3, 'pork', 35, 15)\n",
            "The column:\n",
            "(1, 'chicken', 30, 30)\n",
            "(2, 'beaf', 55, 10)\n"
          ]
        }
      ],
      "source": [
        "import sqlite3\n",
        "\n",
        "conn = sqlite3.connect('BBQ.dp')\n",
        "\n",
        "cursor = conn.cursor()\n",
        "\n",
        "cursor.execute('''\n",
        "  CREATE TABLE IF NOT EXISTS meats (\n",
        "    id INTEGER PRIMARY KEY,\n",
        "    name TEXT,\n",
        "    prize INTEGER,\n",
        "    quantity INTEGER\n",
        "  )''')\n",
        "\n",
        "cursor.execute(\"INSERT INTO meats (name, prize, quantity) VALUES ('chicken', 30, 5)\")\n",
        "cursor.execute(\"INSERT INTO meats (name, prize, quantity) VALUES ('beaf', 55, 10)\")\n",
        "cursor.execute(\"INSERT INTO meats (name, prize, quantity) VALUES ('pork', 40, 15)\")\n",
        "conn.commit()\n",
        "\n",
        "cursor.execute(\"SELECT * FROM meats\")\n",
        "meats = cursor.fetchall()\n",
        "\n",
        "print(\"The column:\")\n",
        "for meat in meats:\n",
        "  print(meat)\n",
        "\n",
        "\n",
        "cursor.execute(\"UPDATE meats SET prize = 35 WHERE name = 'pork'\")\n",
        "cursor.execute(\"UPDATE meats SET quantity = 30 WHERE name = 'chicken'\")\n",
        "conn.commit()\n",
        "\n",
        "cursor.execute(\"SELECT * FROM meats\")\n",
        "meats = cursor.fetchall()\n",
        "\n",
        "print(\"The column:\")\n",
        "for meat in meats:\n",
        "  print(meat)\n",
        "\n",
        "\n",
        "cursor.execute(\"DELETE FROM meats WHERE name = 'pork'\")\n",
        "conn.commit()\n",
        "\n",
        "cursor.execute(\"SELECT * FROM meats\")\n",
        "meats = cursor.fetchall()\n",
        "\n",
        "print(\"The column:\")\n",
        "for meat in meats:\n",
        "  print(meat)\n",
        "\n",
        "cursor.close()\n",
        "conn.close()\n"
      ]
    }
  ]
}
