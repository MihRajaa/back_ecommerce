import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import UserInfo from './types';

type State = {
  userData: UserInfo | null;
};

const initialState: State = { userData: null };

const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    getUserInfo(state: State, action: PayloadAction<UserInfo>) {
      state.userData = action.payload;
    },
  },
});

export default userSlice;
