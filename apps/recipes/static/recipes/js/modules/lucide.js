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
    Printer,
    Share2,
    Facebook,
    BookOpen,
    ImageOff,
    ChevronLeft,
    ChevronRight,
    ArrowLeft,
} from 'https://esm.sh/lucide';

const icons = {
    X,
    Menu,
    ArrowLeft,
    ChefHat,
    Eye,
    Instagram,
    ChevronLeft,
    Share2,
    ChevronRight,
    EyeClosed,
    Facebook,
    ImageOff,
    Printer,
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
