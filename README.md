# ignition

ignition hacks 2023 project

# Start the development server

`npx expo start`

- to use, download the Expo Go app

# Documentation

https://reactnative.dev/docs/environment-setup?guide=quickstart&platform=android

# Note

This app is using Expo Go:
Expo Go: Expo provides cloud build services, which means you can build your app binaries (APK for Android and IPA for iOS) in the cloud without needing to set up local environments. This is especially beneficial for developers without a Mac, as they can still build iOS applications.
Expo Go: If you start with Expo and later realize you need more flexibility, you can "eject" to a bare React Native project. This allows you to add custom native code and modules.

# Use Tailwind

1. Run tailwind-rn in development mode:

   $ npm run dev:tailwind

2. Import TailwindProvider and tailwind.json in the root of your app

import {TailwindProvider} from 'tailwind-rn';
import utilities from './tailwind.json';

3. Wrap the root of your app into TailwindProvider:

   <TailwindProvider utilities={utilities}>
     <MyComponent/>
   </TailwindProvider>

4. Use Tailwind

import {useTailwind} from 'tailwind-rn';

const MyComponent = () => {
const tailwind = useTailwind();

     return <Text style={tailwind('text-blue-600')}>Hello world</Text>;

};
