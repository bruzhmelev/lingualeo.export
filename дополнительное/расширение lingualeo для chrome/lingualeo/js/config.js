// ==UserScript==
// @name LinguaLeoConfig
// @all-frames true
// @include http://*
// @include https://*
// @exclude http*://*facebook.com/plugins/*
// @exclude http*://*twitter.com/widgets/*
// @exclude http*://plusone.google.com/*
// ==/UserScript==

var LinguaLeoConfig = function () {
    var cdnHost = 'https://d144fqpiyasmrr.cloudfront.net',
        apiHost = 'https://api.lingualeo.com',
        siteHost = 'https://lingualeo.com';

    return {
        domain: 'http://lingualeo.com',
		domain_ru: 'http://lingualeo.ru',
		

        path: {
            login: '/login',
            dictionary: '/userdict',
            training: '/training',
            goldStatus: '/gold?from=plagin_meatballs-dialog',
            wordArticle: '/userdict#/{originalText}',
            images: cdnHost + '/plugins/all/images',
            register: '/register',
			register2: '/?utm_source=ll_plagin&utm_medium=referral&utm_campaign=register',
            forgotPass: '/password/forgot',
            meatballs: '/meatballs',
            audio_player: cdnHost + '/plugins/all/flash/1.html#sound='
        },
		
		
		api: apiHost,
        ajax: {
            isAuth: '/isauthorized',
            getTranslations: '/gettranslates',
            translate: '/translate.php',
            addWordToDict: '/addword',
            getUntrainedWordsCount: '/getUntrainedWordsCount',
            setChromeHideCookie: '/setChromeHideCookie',
            login: siteHost + '/api/login',
			checkSiteNotifications: apiHost + '/user/{user_id}/notifications/unread'
        },

        maxTextLengthToTranslate: 50,
        notificationTimeout: 10000,
        untrainedWordsCheckingTimeout: 2 * 60 * 60 * 1000 //two hours
    };
};