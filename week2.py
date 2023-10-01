{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP1dN3fX1yhQUNBdpERFLKn",
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
        "<a href=\"https://colab.research.google.com/github/AngusLing/4111029016_CA/blob/main/week2.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "EnpwcEO0TN5N",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "004467d4-0d71-4c02-c948-fc535a696e38"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please enter logical address: 7000\n",
            "The physical address is 39768\n"
          ]
        }
      ],
      "source": [
        "def memory_addressing(page_table, page_size):\n",
        "\n",
        "  page_table = {0: 5, 1: 9, 2: 14}\n",
        "\n",
        "\n",
        "  logical_address = int(input(\"Please enter logical address: \"))\n",
        "\n",
        "  page_number, offset = divmod(logical_address, page_size)\n",
        "\n",
        "  if page_number in page_table:\n",
        "    frame_number = page_table[page_number]\n",
        "    physical_address = frame_number * page_size + offset\n",
        "    print(f\"The physical address is {physical_address}\")\n",
        "  else:\n",
        "    print(\"Invalid page number, address translation failed.\")\n",
        "\n",
        "page_table = {0: 5, 1: 9, 2: 14}\n",
        "page_size = 4096\n",
        "memory_addressing(page_table, page_size)\n",
        "\n",
        "\n",
        "\n"
      ]
    }
  ]
}
