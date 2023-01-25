# Musical Time Machine With Spotify

This is a program that i learned durining my 100 days of code in python. it is simple and helps users to create a song list in their spotify accounts for special occasaions. You have to login into your Spotify site to generate your won client ID




## Contributing

Contributions are always welcome!














## Installation
You have to install bs4 and spotipy inorder to run this program.


## Documentation

https://pypi.org/project/spotipy/


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

