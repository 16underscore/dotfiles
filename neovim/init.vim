" standard
filetype plugin indent on

set autoindent
set cindent
set incsearch
set hlsearch
set list
set listchars=eol:↵,tab:⇥\ ,trail:·,extends:>,precedes:<,space:·
set noerrorbells
set number
set shiftwidth=3
set showcmd
set smartindent
set smarttab
set softtabstop=3
set tabstop=3

syntax enable
" colorscheme
let g:tokyonight_style = "night"
let g:tokyonight_italic_functions = 1
let g:tokyonight_sidebars = [ "qf", "vista_kind", "terminal", "packer" ]
let g:tokyonight_colors = {'hint': 'orange', 'error': '#ff0000'}
colorscheme tokyonight

hi Normal guibg=None ctermbg=None
" nerdtree
autocmd VimEnter * NERDTree | wincmd p
autocmd BufEnter * if tabpagenr ('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
autocmd BufEnter * if winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
autocmd BufWinEnter * if getcmdwintype() == '' | silent NERDTreeMirror | endif
