# mkdocs-vim-md-tags-plugin

An MkDocs plugin that generates a vim tags file for autocompleting and navigating through markdown pages.

![demo](demo/mkdocs_vim_md_tags_demo.gif)

The above demo shows how the plugin can be used to rapidly develop wiki-style interconnected pages in a very organic way. While writing the `space` article, the author decides to link to a new article called `universe`, for which a file does not yet exist. So the author creates the file, and---as long as an instance of `mkdocs serve` is running in the background---the plugin generates a new tags file that includes `universe.md`, which the author can then navigate to and begin filling out the new article. 

This way of authoring pages allows for articles to be highly interconnected. The best time to contextually link between articles is while the content is being generated. No one is going to come back and link together pages after the fact. This plugin allows for these connections to be created in a very straightforward and easy manner.

This plugin takes advantage of vim's build in tag system. type `:help tags` while in vim for more information on tags. For the purposes of this plugin, the two most imporant keybindings to remember are:

`Ctrl+]` - This command jumps to the tag underneath the cursor.

`Ctrl+t` - This command returns to the previous entry in the tag stack.

## Install the Plugin

Install the plugin using pip:

`pip install mkdocs-vim-md-tags-plugin`

Activate the plugin in `mkdocs.yml`:
```yaml
plugins:
  - search
  - vim-md-tags
```

> **Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.

More information about plugins in the [MkDocs documentation][mkdocs-plugins].

## Add tag file to vim
Edit your vimrc file
```sh
vim ~/.vimrc
```

Add this plugin's tags file to the list of tags
```
set tags=./md_tags;/
```
vim should now recursively load the tags file as long as it was started from somewhere in the MkDocs site structure from which it was generated.

## Getting YouCompleteMe autocomplete
If you use YouCompleteMe, you can tell it to load the tags file to get autocompletion of the markdown file names by adding the following to your `~/.vimrc`
```
let g:ycm_collect_identifiers_from_tags_files = 1
let g:ycm_filetype_blacklist = {}
``` 

## Config

* `tag_file` - Sets the filename of the tags file to be generated

## See Also

More information about templates [here][mkdocs-template].

More information about blocks [here][mkdocs-block].

[mkdocs-plugins]: http://www.mkdocs.org/user-guide/plugins/
[mkdocs-template]: https://www.mkdocs.org/user-guide/custom-themes/#template-variables
[mkdocs-block]: https://www.mkdocs.org/user-guide/styling-your-docs/#overriding-template-blocks
