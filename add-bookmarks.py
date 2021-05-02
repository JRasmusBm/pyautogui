import pyautogui as gui
from time import sleep

bookmarks = [
    ("ambv/black", "https://github.com/ambv/black"),
    ("neovim/nvim-lspconfig", "https://github.com/neovim/nvim-lspconfig"),
    ("nvim-lua/completion-nvim", "https://github.com/nvim-lua/completion-nvim"),
    ("tjdevries/nlua.nvim", "https://github.com/tjdevries/nlua.nvim"),
    (
        "tjdevries/lsp_extensions.nvim",
        "https://github.com/tjdevries/lsp_extensions.nvim",
    ),
    (
        "nvim-treesitter/nvim-treesitter",
        "https://github.com/nvim-treesitter/nvim-treesitter",
    ),
    ("nvim-treesitter/playground", "https://github.com/nvim-treesitter/playground"),
    ("puremourning/vimspector", "https://github.com/puremourning/vimspector"),
    ("szw/vim-maximizer", "https://github.com/szw/vim-maximizer"),
    ("rust-lang/rust.vim", "https://github.com/rust-lang/rust.vim"),
    ("tweekmonster/gofmt.vim", "https://github.com/tweekmonster/gofmt.vim"),
    ("tpope/vim-fugitive", "https://github.com/tpope/vim-fugitive"),
    ("junegunn/gv.vim", "https://github.com/junegunn/gv.vim"),
    ("vim-utils/vim-man", "https://github.com/vim-utils/vim-man"),
    ("mbbill/undotree", "https://github.com/mbbill/undotree"),
    ("vuciv/vim-bujo", "https://github.com/vuciv/vim-bujo"),
    ("tpope/vim-dispatch", "https://github.com/tpope/vim-dispatch"),
    ("theprimeagen/vim-be-good", "https://github.com/theprimeagen/vim-be-good"),
    ("gruvbox-community/gruvbox", "https://github.com/gruvbox-community/gruvbox"),
    (
        "octol/vim-cpp-enhanced-highlight",
        "https://github.com/octol/vim-cpp-enhanced-highlight",
    ),
    ("tpope/vim-projectionist", "https://github.com/tpope/vim-projectionist"),
    ("nvim-lua/popup.nvim", "https://github.com/nvim-lua/popup.nvim"),
    (
        "nvim-telescope/telescope.nvim",
        "https://github.com/nvim-telescope/telescope.nvim",
    ),
    (
        "nvim-telescope/telescope-fzy-native.nvim",
        "https://github.com/nvim-telescope/telescope-fzy-native.nvim",
    ),
    (
        "colepeters/spacemacs-theme.vim",
        "https://github.com/colepeters/spacemacs-theme.vim",
    ),
    ("sainnhe/gruvbox-material", "https://github.com/sainnhe/gruvbox-material"),
    ("phanviet/vim-monokai-pro", "https://github.com/phanviet/vim-monokai-pro"),
    ("flazz/vim-colorschemes", "https://github.com/flazz/vim-colorschemes"),
    ("chriskempson/base16-vim", "https://github.com/chriskempson/base16-vim"),
    ("dracula/vim", "https://github.com/dracula/vim"),
    ("mhinz/vim-rfc", "https://github.com/mhinz/vim-rfc"),
    ("ThePrimeagen/neovim-irc-ui", "https://github.com/ThePrimeagen/neovim-irc-ui"),
    ("sbdchd/neoformat", "https://github.com/sbdchd/neoformat"),
]

gui.hotkey("alt-tab", "tab")

for name, link in bookmarks:
    sleep(0.05)
    gui.click(x=330, y=214, button="right")
    gui.click(x=386, y=239, button="left")
    gui.write(name)
    gui.hotkey("tab")
    gui.write(link)
    gui.hotkey("enter")
