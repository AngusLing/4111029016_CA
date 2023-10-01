{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOwXLpm/2/ImomgyaqpOqoX",
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
        "<a href=\"https://colab.research.google.com/github/AngusLing/4111029016_CA/blob/main/Untitled4.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iYQPHwFwj4m3",
        "outputId": "01e899c0-e059-4d59-8390-b3c984a8adf4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "homework.txt\n",
            "21\n",
            "1695314087.3918178\n",
            "Thu Sep 21 16:34:47 2023\n"
          ]
        }
      ],
      "source": [
        "import os\n",
        "import time\n",
        "import shutil\n",
        "\n",
        "os.makedirs('CS/homework.txt', exist_ok=True)\n",
        "\n",
        "with open('homework.txt', 'w') as file:\n",
        "  file.write('4111029016_凌敏修\\n')\n",
        "\n",
        "with open('homework.txt', 'r') as file:\n",
        "  content = file.read()\n",
        "\n",
        "file = open('homework.txt', 'r')\n",
        "content = file.read()\n",
        "\n",
        "with open('homework.txt', 'r') as file:\n",
        "  content = file.read()\n",
        "\n",
        "items = os.listdir('CS')\n",
        "\n",
        "for item in items:\n",
        "  print(item)\n",
        "\n",
        "file_size = os.path.getsize('homework.txt')\n",
        "print(file_size)\n",
        "\n",
        "modification_time = os.path.getmtime('homework.txt')\n",
        "print(modification_time)\n",
        "\n",
        "formatted_time = time.ctime(modification_time)\n",
        "print(formatted_time)\n",
        "\n",
        "if os.path.exists('homework.txt'):\n",
        "  os.remove('homework.txt')\n",
        "\n",
        "shutil.rmtree('CS')\n"
      ]
    }
  ]
}
