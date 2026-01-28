import {
    createIcons,
    X,
    ChefHat,
    Eye,
    Menu,
    EyeClosed,
    User,
    Users,
    Filter,
    Sparkle,
    Instagram,
    Facebook,
    BookOpen,
} from 'https://esm.sh/lucide';

const icons = {
    X,
    Menu,
    ChefHat,
    Eye,
    Instagram,
    EyeClosed,
    Facebook,
    User,
    Users,
    Sparkle,
    BookOpen,
    Filter,
};

export function lucideDev() {
    createIcons({
        icons,
    });
}

export function refreshLucide() {
    createIcons({ icons });
}
