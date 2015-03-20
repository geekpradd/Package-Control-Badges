##Package Control Badges

This is a Flask app that allows you to add badges to your Sublime Text Plugins showing your Plugin Downloads. This is very easy to use using the API and the API is hosted on Heroku.

###Demo

<a href="https://packagecontrol.io/packages/Terminal"><img src="https://packagecontrol.herokuapp.com/downloads/Terminal.svg"></a>

The source for the above is:

```html
<a href="https://packagecontrol.io/packages/Terminal"><img src="https://packagecontrol.herokuapp.com/downloads/Terminal.svg"></a>
```

###API Endpoints

The base API endpoints are (currently only for downloads):

```
https://packagecontrol.herokuapp.com/downloads/[Package name].[format]
```

The package name needs to be quoted, like `Theme - Soda` becomes `Theme%20-%20Soda` 

Formats currently supported are:

- PNG
- SVG
- JPEG
- GIF
- TIFF

####Colors

You can also change the color of the badge by adding a `color` parameter. The value of this URL parameter is valid CSS hexadecimal color or a normal color name like `17024F` (without the #) or `red`

Example:

<a href="https://packagecontrol.io/packages/HTML%20Minifier"><img src="https://packagecontrol.herokuapp.com/downloads/HTML%20Minifier.svg?color=EF9F9F"></a>

Source:

```html
<a href="https://packagecontrol.io/packages/HTML%20Minifier"><img src="https://packagecontrol.herokuapp.com/downloads/HTML%20Minifier.svg?color=EF9F9F"></a>
```

####Styles

There are 3 main styles available to choose from (as given in shields.io):

1. Flat (default)
2. Plastic (legacy)
3. Flat-Square

You can change the styles by adding a `style` parameter after the URL.

Example:

<a href="https://packagecontrol.io/packages/HTML%20Minifier"><img src="https://packagecontrol.herokuapp.com/downloads/HTML%20Minifier.svg?color=red&style=flat-square"></a>

Source:

```html
<a href="https://packagecontrol.io/packages/HTML%20Minifier"><img src="https://packagecontrol.herokuapp.com/downloads/HTML%20Minifier.svg?color=red&style=flat-square"></a>
```

The value of the `style` paramter will be either `plastic`, `flat` or `flat-square`

###To-Do

1. Add more features (that is, endpoints)
2. Add alternate hosting (on OpenShift) to compensate Heroku Free tier limits

###About

Created By Pradipta (geekpradd). Copyright 2015. MIT Licensed.